# inventory
A lightweight property inventory helper

## Still in development (v0.\*), *so expect things to not work*

This app is for assisting SCA branches in managing both annual inventories and pack-in/pack-out at events. It is designed to be installed on a portable machine (a $35 Raspberry Pi fits the bill nicely here, but spend the extra $10 for a case) to be taken to events and serve up web pages with inventory information without needing access to the Internet.

See it in action at https://cordelya.pythonanywhere.com

Want to try it out? Scroll to the bottom!

Items are grouped into Boxes (can be literal or virtual boxes), which are then further grouped into Warehouses. In this context, a warehouse is a geographic location where a box or boxes are stored. A branch cargo trailer full of items is a Warehouse. Examples of virtual boxes include the "loose in the trailer" box, the "driver-side cargo rack" box, or the "gold-key-closet" box. 

Key: (I) = implemented
     (N) = not yet implemented

(I/N) notations updated 9/18/2020 at close of coding day.

* (I) Tracks whether items are consumable or not
* (I) Tracks the replacement value of each item. Front-end displays total aggregate value on index, and sub-values on Warehouse and Box detail pages.
* (I) Set keywords to make search results filter-able. Add as many keywords as applicable. Suggested keywords include "Category: <category>" for categories like "kitchen" "archery" "heraldic" etc; "Color: <color>" to classify items by their main color(s); "Material: <material>" to classify by material (glass, metal, plastic, etc)
  * (N) Keywords show on item detail page
  * (N) Keyword detail pages list all items
* (I) Move items from one box to another by updating the current box's end date and creating a new items_in_boxes record for the new box, leaving the end date blank. Item's box history will be preserved. Front end shows only current location.
* Reports: 
  * (N) entire inventory arranged by warehouse and box with no orphaned tables or optionally starting a new page every box
  * (N) export entire inventory to .csv for spreadsheet-friendly backup. Filter by keywords, Warehouses, boxes. Group by Warehouse or Box (NOTE: .csv does not support multiple sheets per file, so if you request grouping by Warehouse or by Box, you will receive multiple .csv files - one for each group object.)
  * (I) export database as database-friendly backup file (available on command-line)
  * (N) consumable items, per box, for printing to allow event staff or annual inventory staff to verify quantities remaining and make notes.
  * (I) consumable items, filtered to show items which are running low, to use as a shopping list for replenishment
* (N) Pack-out friendly search: when item arrives for packing, begin search with general item description (ie "ladle"), then narrow search by keyword (Category: Kitchen, Material: Metal, etc.) until matching item is identified (verify visually via inline photo) and place item in indicated box. Can go very quickly if a person familiar with the system is staffing the search terminal.
 * (N) Warehouse detail page shows photo associated with warehouse. This could be an image of an individual's or officer's armory, or a photo of the physical warehouse.
 * (N) Box listing on warehouse detail, box list, and box detail includes photo of box, if set.
 * (I) Item listing on box detail, item list, and item detail shows photo if set. Set photo by saving images to /static/inv/img and recording the image's filename in the item's record. Recommended image file naming convention: by item ID, item name, or combo. Image name field and image name (including extension, but excluding path) must match exactly. Run python manage.py collectstatic after adding any files to the static/ folder tree. If image is not set, helper text asks viewer to snap a photo of the item and email it to the inventory management contact with the item's id number in the subject line (item id number is displayed).
 
 How to get it: (note: I haven't run through this procedure from start to finish yet - let me know if I've missed a step somewhere)
 Requirements: 
 * Python3[.6|.7|.8] (get the latest you can, but 3.6 is still supported if that's what you've got.)
 * Git
 * Pip
 * Django
 
 in the folder where you want to install the app (it comes with a top-level folder called "inventory")
 
 ````
 $ git clone https://github.com/Cordelya/inventory.git
 ````
 
Copy credentials-example.py to credentials.py and enter a generated secret key in the file, inside the single quotes, overwriting "paste your secret key here". Search "django secret key generator" if you need help with that.

````
$ python manage.py migrate
$ python manage.py createsuperuser # create a user account so you can add items to the database using the admin web interface. Don't forget the login details!
$ python manage.py runserver
````

Head to 127.0.0.1:8000/admin and log in

Begin by adding at least one warehouse. Add at least one box to one warehouse. Add some keywords. Add at least one item (and associate it with a box and keywords in the same form).

Suggested keywords include:
* categories structured as Category: Category, so kitchen items might use a category keyword of Category: Kitchen
* colors structured as Color: Color, so an item that is blue and red might use Color: Blue and Color: Red
* materials structured as Material: Material, so an item that is glass might use Material: Glass

You can add as many keywords as you want to each item. If you want to mark some items that need attention, you could assign them a "TODO" keyword and then filter on the "TODO" keyword later on.

A note about items and quantities:

If you have 15 non-disposable water pitchers that are all the same, you can put them in one item record. Set the quantity to 15 and leave the "percent remaining" field at 100. 
If you have 200 disposable plastic cups, but a "full" supply of cups is 500, you can enter 500 as the quantity, check the "consumable" box, and then enter 40 in the "percent remaining" field. 

If you have a roll of plastic cling wrap, enter 1 as the quantity, and estimate how much is left on the roll for the "percent remaining" field. Check the "consumable" box.
When you view the consumables shopping list (check the feature list - it might not be built yet), you will see all of the consumable items, their "full" quantity, and their percent remaining. If the item count is greater than 1, the quantity needed will be calculated based on the "full" quantity and percentage remaining so your restocking shopper will know how many of each item they need to buy.
