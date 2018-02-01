var setfoldBehaviour = setInterval(setEvents, 1000);

function setEvents() {
    console.log('Setting js events...');
    document.getElementById('fold-img-container').onclick = hideSideBar;
    clearInterval(setfoldBehaviour);
}

function hideSideBar() {
    // effect to rotate to the left

    // change size of the button and apply a border radius


    // hide side bar
    var side_bar = document.getElementById('side-bar-content')
    if (side_bar.style.display == 'none') side_bar.style.display = 'block';
    else side_bar.style.display = 'none';
}
