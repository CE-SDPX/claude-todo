"""UI end-to-end tests — Red phase (Playwright).

These tests define the expected behaviour of the UI.
Run them before implementing any UI code:

    pytest tests/e2e/ -v

The `live_server` session fixture starts uvicorn automatically.
Every test should FAIL until the UI components are implemented.
Do not modify these tests during the Green phase.

Setup (one-time):
    pip install playwright pytest-playwright
    playwright install chromium
"""

import subprocess
import time

import pytest
import pytest_asyncio
from playwright.async_api import Page, async_playwright, expect


# ---------------------------------------------------------------------------
# Session-scoped fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def live_server():
    """Start a uvicorn server on port 18000 for the entire test session."""
    proc = subprocess.Popen(
        [
            "python", "-m", "uvicorn", "src.main:app",
            "--port", "18000",
            "--log-level", "warning",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(2)  # wait for the server to be ready
    yield "http://localhost:18000"
    proc.terminate()
    proc.wait()


@pytest_asyncio.fixture
async def page(live_server):
    """Provide a fresh Playwright page pointed at the live server."""
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        context = await browser.new_context()
        pg = await context.new_page()
        await pg.goto(live_server)
        yield pg
        await browser.close()


# ---------------------------------------------------------------------------
# AC-UI-01  Add todo
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_ui_form_add_todo_appears_in_list(page: Page):
    """Adding a todo must show it in the list immediately (AC-UI-01)."""
    await page.fill("[data-testid=todo-input]", "Buy oat milk")
    await page.click("[data-testid=add-button]")
    await expect(page.locator("[data-testid=todo-item]")).to_contain_text("Buy oat milk")


@pytest.mark.asyncio
async def test_ui_form_clears_input_after_successful_add(page: Page):
    """The input field must be empty after a successful add."""
    await page.fill("[data-testid=todo-input]", "Task X")
    await page.click("[data-testid=add-button]")
    await expect(page.locator("[data-testid=todo-input]")).to_have_value("")


@pytest.mark.asyncio
async def test_ui_form_empty_title_shows_error_and_sends_no_request(page: Page):
    """Submitting an empty title must show a validation error and not add a new item (AC-UI-06)."""
    initial_count = await page.locator("[data-testid=todo-item]").count()
    await page.click("[data-testid=add-button]")
    await expect(page.locator("[data-testid=form-error]")).to_be_visible()
    assert await page.locator("[data-testid=todo-item]").count() == initial_count


# ---------------------------------------------------------------------------
# AC-UI-02  Toggle status
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_ui_checkbox_check_adds_done_class_to_item(page: Page):
    """Checking a checkbox must add the 'done' class to the todo item (AC-UI-02)."""
    await page.fill("[data-testid=todo-input]", "Toggle me")
    await page.click("[data-testid=add-button]")
    item = page.locator("[data-testid=todo-item]", has_text="Toggle me")
    await item.locator("[data-testid=todo-checkbox]").check()
    await expect(item).to_have_class("done")


@pytest.mark.asyncio
async def test_ui_checkbox_uncheck_removes_done_class(page: Page):
    """Unchecking a checkbox must remove the 'done' class."""
    await page.fill("[data-testid=todo-input]", "Toggle back")
    await page.click("[data-testid=add-button]")
    item = page.locator("[data-testid=todo-item]", has_text="Toggle back")
    checkbox = item.locator("[data-testid=todo-checkbox]")
    await checkbox.check()
    await checkbox.uncheck()
    await expect(item).not_to_have_class("done")


# ---------------------------------------------------------------------------
# AC-UI-03  Delete
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_ui_delete_button_removes_item_from_list(page: Page):
    """Clicking delete must remove the item from the list (AC-UI-03)."""
    await page.fill("[data-testid=todo-input]", "Delete me")
    await page.click("[data-testid=add-button]")
    item = page.locator("[data-testid=todo-item]", has_text="Delete me")
    await item.hover()
    await item.locator("[data-testid=delete-button]").click()
    await expect(
        page.locator("[data-testid=todo-item]", has_text="Delete me")
    ).to_have_count(0)


# ---------------------------------------------------------------------------
# AC-UI-04  Filter by status
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_ui_filter_done_shows_only_done_items(page: Page):
    """Clicking the Done tab must show only done items (AC-UI-04)."""
    await page.fill("[data-testid=todo-input]", "Pending task")
    await page.click("[data-testid=add-button]")
    await page.fill("[data-testid=todo-input]", "Done task")
    await page.click("[data-testid=add-button]")

    done_item = page.locator("[data-testid=todo-item]", has_text="Done task")
    await done_item.locator("[data-testid=todo-checkbox]").check()

    await page.click("[data-testid=filter-done]")
    await expect(page.locator("[data-testid=todo-item]")).to_have_count(1)
    await expect(page.locator("[data-testid=todo-item]")).to_contain_text("Done task")


@pytest.mark.asyncio
async def test_ui_filter_pending_shows_only_unchecked_items(page: Page):
    """Clicking the Pending tab must show only pending items."""
    await page.fill("[data-testid=todo-input]", "Active task")
    await page.click("[data-testid=add-button]")
    await page.click("[data-testid=filter-pending]")
    items = page.locator("[data-testid=todo-item]")
    count = await items.count()
    for i in range(count):
        checkbox = items.nth(i).locator("[data-testid=todo-checkbox]")
        assert not await checkbox.is_checked()


# ---------------------------------------------------------------------------
# AC-UI-05  Keyword search
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_ui_search_filters_list_by_keyword(page: Page):
    """Typing a keyword must filter the list to matching titles (AC-UI-05)."""
    await page.fill("[data-testid=todo-input]", "Buy groceries")
    await page.click("[data-testid=add-button]")
    await page.fill("[data-testid=todo-input]", "Do laundry")
    await page.click("[data-testid=add-button]")

    await page.fill("[data-testid=search-input]", "groceries")
    await page.wait_for_timeout(400)  # wait for debounce

    items = page.locator("[data-testid=todo-item]")
    count = await items.count()
    for i in range(count):
        text = await items.nth(i).locator("[data-testid=todo-title]").text_content()
        assert "groceries" in text.lower()


# ---------------------------------------------------------------------------
# Inline edit
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_ui_double_click_title_shows_edit_input(page: Page):
    """Double-clicking a title must replace it with an edit input."""
    await page.fill("[data-testid=todo-input]", "Edit me")
    await page.click("[data-testid=add-button]")
    await page.locator("[data-testid=todo-title]", has_text="Edit me").dblclick()
    await expect(page.locator("[data-testid=todo-edit-input]")).to_be_visible()


@pytest.mark.asyncio
async def test_ui_inline_edit_enter_saves_new_title(page: Page):
    """Pressing Enter in the edit input must save the new title."""
    await page.fill("[data-testid=todo-input]", "Old title")
    await page.click("[data-testid=add-button]")
    await page.locator("[data-testid=todo-title]", has_text="Old title").dblclick()
    edit = page.locator("[data-testid=todo-edit-input]")
    await edit.fill("New title")
    await edit.press("Enter")
    await expect(
        page.locator("[data-testid=todo-title]", has_text="New title")
    ).to_be_visible()


@pytest.mark.asyncio
async def test_ui_inline_edit_escape_cancels_change(page: Page):
    """Pressing Escape in the edit input must restore the original title."""
    await page.fill("[data-testid=todo-input]", "Keep this title")
    await page.click("[data-testid=add-button]")
    await page.locator("[data-testid=todo-title]", has_text="Keep this title").dblclick()
    edit = page.locator("[data-testid=todo-edit-input]")
    await edit.fill("Should not save")
    await edit.press("Escape")
    await expect(
        page.locator("[data-testid=todo-title]", has_text="Keep this title")
    ).to_be_visible()
