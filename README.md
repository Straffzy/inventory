# inventory
A lightweight property inventory helper

## Still in development (v0.\*), *so expect things to not work*

Designed to help SCA branches manage both annual inventories and pack-in/pack-out at events, this app keeps track of items, grouping them into Boxes (can be literal or virtual boxes), which are then further grouped into Warehouses. Think of Warehouses as locations where Boxes are stored. Does your branch have a cargo trailer full of items? The trailer is a Warehouse.

* Tracks whether items are consumable or not
* Tracks the replacement value of each item for (future enhancement): displaying the total replacement value - for insurance
* Set keywords to make search results filter-able. Add as many keywords as applicable. Suggested keywords include "Category: <category>" for categories like "kitchen" "archery" "heraldic" etc; "Color: <color>" to classify items by their main color(s); "Material: <material>" to classify by material (glass, metal, plastic, etc)
* Display a photo of each item by saving images to /static/inv/img and recording the image's filename in the item's record. Recommended image file naming convention: by item ID, item name, or combo
* Move items from one box to another by updating the current box's end date and creating a new items_in_boxes record for the new box, leaving the end date blank. Item's box history will be preserved.
* Reports: 
  * entire inventory arranged by warehouse and box with no orphaned tables or optionally starting a new page every box
  * export entire inventory to .csv for spreadsheet-friendly backup. Filter by keywords, Warehouses, boxes. Group by Warehouse or Box (NOTE: .csv does not support multiple sheets per file, so if you request grouping by Warehouse or by Box, you will receive multiple .csv files - one for each group object.)
  * export database as database-friendly backup file
  * consumable items, per box, for printing to allow event staff or annual inventory staff to verify quantities remaining and make notes.
  * consumable items, filtered to show items which are running low, to use as a shopping list for replenishment
* Pack-out friendly search: when item arrives for packing, begin search with general item description (ie "ladle"), then narrow search by keyword (Category: Kitchen, Material: Metal, etc.) until matching item is identified (verify visually via inline photo) and place item in indicated box.

