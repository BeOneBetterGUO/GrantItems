    function adjustImageSize(img) {
        const card = img.closest('.card'); // 找到.card元素
        const cardHeight = card.offsetHeight; // 获取.card的高度
        const cardWidth = card.offsetWidth; // 获取.card的宽度

        if (img.naturalHeight > img.naturalWidth) {
            img.style.width = `${cardWidth}px`;   // 宽度与.card相同
            img.style.height = 'auto';             // 高度自适应
        } else {
            img.style.height = `${cardHeight}px`;  // 高度与.card相同
            img.style.width = 'auto';               // 宽度自适应
        }
    }