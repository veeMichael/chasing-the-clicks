const clicks = document.getElementById('btn');
const clickCount = document.getElementById('clickCount');

// Check if the click count is stored in localStorage
if (localStorage.getItem('clickCount')) {
  clickCount.innerHTML = localStorage.getItem('clickCount');
}

// Increase clicks by 1 every time the button is clicked
clicks.addEventListener('click', () => {
  let count = parseInt(clickCount.innerHTML);
  count++;
  clickCount.innerHTML = count;
  // Store the click count in localStorage
  localStorage.setItem('clickCount', count);

  // Update the click count in the server-side database
  // fetch('/update_click_count/')
  //   .then(response => response.json())
  //   .then(data => console.log(data))
  //   .catch(error => console.error(error));
});
