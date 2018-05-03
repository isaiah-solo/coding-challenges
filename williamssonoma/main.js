// Starts with title and gathers json data
const title = data.name;
const groups = data.groups;

var titleDiv = document.getElementById('title');
titleDiv.style.textAlign = 'center';
titleDiv.innerHTML = title;

var itemList = document.getElementById('item-list');

// Class to hold json item
class Item {
  constructor(group) {
    this.selected = 0;
    this.id = group.id;
    this.name = group.name;
    this.thumbnail = group.thumbnail;
    this.hero = group.hero;
    this.links = group.links;
    this.images = group.images;
    this.sellingPrice = group.hasOwnProperty('price')
                       ? '$' + group.price.selling
                       : '$' + group.priceRange.selling.low + ' - $' + group.priceRange.selling.high;
    this.regularPrice = group.hasOwnProperty('price')
                       ? '$' + group.price.regular
                       : '$' + group.priceRange.regular.low + ' - $' + group.priceRange.regular.high;
    this.priceType = group.hasOwnProperty('price')
                      ? group.price.type
                      : group.priceRange.type;
  }
}

// Handles clicking out of carousel dialog
window.addEventListener('click', function(e){   
  let dialog = document.getElementById('box');

  if (dialog.contains(e.target) || flag){
    flag = false;
  } else {
    dialog.style.display = 'none';
    const content = document.getElementById('content');
    content.style.filter = 'brightness(100%)';
    let thumbnailsDiv = document.getElementsByClassName('dialog-thumbnails')[0];
    thumbnailsDiv.parentNode.removeChild(thumbnailsDiv);
  }
});

// Flag for above function
let flag = false;

// Function that loads image from json
const loadImage = (div, image) => {
  div.src = image.href;
  div.alt = image.alt;
  div.meta = image.meta;
  div.rel = image.rel;
  div.size = image.size;
}

// Function that changes dialog main image
const changeMainImage = (div, item) => {
  const selected = item.images[item.selected];
  loadImage(div, selected);
};    

// Find child thumbnail based on selected variable
const findChild = (div, item) => {
  let current = div.firstChild;
  let counter = 0;

  while (counter < item.selected) {
    current = current.nextSibling;
    counter++;
  }

  return current;
}

// Iterate through and chooses selected thumbnail
const chooseThumbnail = (target, item) => {
  let child = target;
  let thumbnailCounter = 0;

  while ((child = child.previousSibling) != null) {
    thumbnailCounter++;
    child.style.border = '1px solid white';
  }

  child = target;

  while ((child = child.nextSibling) != null) {
    child.style.border = '1px solid white';
  }

  item.selected = thumbnailCounter;

  target.style.border = '1px solid red';
};

// Loop through each item and create page listing
for (let group of groups) {
  const item = new Item(group);

  const itemDiv = document.createElement('div');
  itemDiv.className = 'item';
  itemDiv.id = item.id;

  const itemImage = document.createElement('img');
  loadImage(itemImage, item.hero);
  itemImage.className = 'item-image';
  itemDiv.appendChild(itemImage);

  // Handles image click
  itemImage.addEventListener('click', (event) => {
    flag = true;
    const dialog = document.getElementById('box');
    const content = document.getElementById('content');
    const mainImageContainer = document.getElementById('dialog-main-image-container');
    const mainImage = document.getElementById('dialog-main-image');

    const thumbnailsDiv = document.createElement('div');
    thumbnailsDiv.className = 'dialog-thumbnails';
    dialog.appendChild(thumbnailsDiv);

    dialog.style.display = 'block';
    content.style.filter = 'brightness(50%)';

    let selectedCounter = 0;

    for (let image of item.images) {
      const thumbnailDiv = document.createElement('img');
      thumbnailDiv.style.border = '1px solid ' + (selectedCounter++ === item.selected ? 'red' : 'white');
      loadImage(thumbnailDiv, image);
      thumbnailDiv.className = 'dialog-thumbnail';
      thumbnailsDiv.appendChild(thumbnailDiv);

      // Handles thumbnail click
      thumbnailDiv.addEventListener('click', (event2) => {
        chooseThumbnail(event2.target, item);
        changeMainImage(mainImage, item);
      });

      // Handles left arrow click
      let leftArrow = document.createElement('div');
      leftArrow.className = 'dialog-left-arrow';
      leftArrow.addEventListener('click', (e) => {
        if (item.selected <= 0)
          return;

        item.selected--;

        let child = findChild(thumbnailsDiv, item);
        chooseThumbnail(child, item);
        changeMainImage(mainImage, item);
      });

      // Handles right arrow click
      let rightArrow = document.createElement('div');
      rightArrow.className = 'dialog-right-arrow';
      rightArrow.addEventListener('click', (e) => {
        if (item.selected >= item.images.length - 1)
          return;

        item.selected++;

        let child = findChild(thumbnailsDiv, item);
        chooseThumbnail(child, item);
        changeMainImage(mainImage, item);
      });

      mainImageContainer.appendChild(leftArrow);
      mainImageContainer.appendChild(rightArrow);
    }

    changeMainImage(mainImage, item);
  });

  const itemName = document.createElement('h4');
  itemName.className = 'item-name';
  itemName.innerHTML = item.name;
  itemDiv.appendChild(itemName);

  if (item.priceType === 'special') {
    const itemOriginalPrice = document.createElement('div');
    itemOriginalPrice.className = 'prices';
    itemOriginalPrice.style.color = 'grey';
    itemOriginalPrice.innerHTML = item.regularPrice
    itemDiv.appendChild(itemOriginalPrice);
  }

  const itemSellingPrice = document.createElement('div');
  itemSellingPrice.className = 'prices';
  itemSellingPrice.innerHTML = (item.priceType === 'special' ? 'Special ' : '') + item.sellingPrice;
  itemDiv.appendChild(itemSellingPrice);

  itemList.appendChild(itemDiv);
}