# inventory_system.py
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Global inventory: item_name -> quantity
stock_data: Dict[str, int] = {}

def add_item(item: str, qty: int = 0, logs: Optional[List[str]] = None) -> None:
    #Add qty of item to stock_data
    if logs is None:
        logs = []

    if not isinstance(item, str) or not item:
        raise TypeError("item must be a non-empty string")

    try:
        qty = int(qty)
    except (TypeError, ValueError):
        raise ValueError("qty must be an integer or convertible to int")

    prev = stock_data.get(item, 0)
    stock_data[item] = prev + qty
    timestamp = datetime.now().isoformat()
    entry = f"{timestamp}: Added {qty} of {item} (previous {prev}, now {stock_data[item]})"
    logs.append(entry)
    logger.info(entry)

def remove_item(item: str, qty: int) -> None:
    """Remove qty of item from stock_data. Raises KeyError or ValueError on invalid operations."""
    if not isinstance(item, str) or not item:
        raise TypeError("item must be a non-empty string")

    try:
        qty = int(qty)
    except (TypeError, ValueError):
        raise ValueError("qty must be an integer or convertible to int")

    if item not in stock_data:
        raise KeyError(f"Item '{item}' not found in inventory")

    if qty < 0:
        raise ValueError("qty must be non-negative for removal")

    stock_data[item] -= qty
    logger.info(f"Removed {qty} of {item}; remaining {stock_data.get(item, 0)}")

    if stock_data[item] <= 0:
        del stock_data[item]
        logger.info(f"{item} removed from inventory because quantity is <= 0")

def get_qty(item: str) -> int:
    """Return quantity for item. Returns 0 if item not present."""
    if not isinstance(item, str) or not item:
        raise TypeError("item must be a non-empty string")

    return stock_data.get(item, 0)

def load_data(file: str = "inventory.json") -> None:
    """Load inventory from a JSON file. If file missing or invalid, leaves stock_data unchanged and logs error."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("inventory file must contain a JSON object mapping items to quantities")
            cleaned: Dict[str, int] = {}
            for k, v in data.items():
                if not isinstance(k, str):
                    logger.warning("Skipping non-string key in inventory: %r", k)
                    continue
                try:
                    cleaned[k] = int(v)
                except (TypeError, ValueError):
                    logger.warning("Invalid quantity for %s: %r — defaulting to 0", k, v)
                    cleaned[k] = 0
            stock_data = cleaned
            logger.info("Loaded inventory from %s", file)
    except FileNotFoundError:
        logger.warning("Inventory file %s not found. Starting with empty inventory.", file)
    except json.JSONDecodeError as exc:
        logger.error("Failed to parse JSON from %s: %s", file, exc)
    except Exception as exc:
        logger.exception("Unexpected error while loading data: %s", exc)

def save_data(file: str = "inventory.json") -> None:
    """Save current stock_data to file as JSON. Handles IO errors gracefully."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=2)
        logger.info("Saved inventory to %s", file)
    except Exception as exc:
        logger.exception("Failed to save inventory to %s: %s", file, exc)

def print_data() -> None:
    print("Items Report")
    for name, qty in stock_data.items():
        print(f"{name} -> {qty}")

def check_low_items(threshold: int = 5) -> List[str]:
    try:
        threshold = int(threshold)
    except (TypeError, ValueError):
        raise ValueError("threshold must be an integer")
    return [name for name, qty in stock_data.items() if qty < threshold]

def main() -> None:
    logs: List[str] = []
    try:
        load_data()

        add_item("apple", 10, logs)
        add_item("banana", 5, logs)

        try:
            remove_item("apple", 3)
        except KeyError:
            logger.warning("Tried to remove an item that does not exist")

        print("Apple stock:", get_qty("apple"))
        print("Low items:", check_low_items())

        save_data()
        print_data()

        logger.info("Activity logs: %s", logs)

    except Exception as exc:
        logger.exception("Unhandled exception in main: %s", exc)

if __name__ == "__main__":
    main()
