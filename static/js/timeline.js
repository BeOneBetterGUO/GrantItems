document.addEventListener('DOMContentLoaded', function() {
    const items = document.querySelectorAll('.container-second p');
    let closestItem = null;
    let closestDateDiff = Infinity;
    const today = new Date();

    items.forEach(item => {
        const dateText = item.textContent.split('————')[0];
        const itemDate = new Date(dateText);
        const dateDiff = Math.abs(itemDate - today);

        if (dateDiff < closestDateDiff) {
            closestDateDiff = dateDiff;
            closestItem = item;
        }
    });

    if (closestItem) {
        closestItem.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
});
