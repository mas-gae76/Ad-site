let nav = document.getElementById('pc_nav');
nav.addEventListener('click', function (event) {
    let target = event.target;
    let targetParent = target.closest('.menu-item');

    if (targetParent) {
        let subMenu = targetParent.getElementsByClassName('submenu')[0];
        close();
        if (subMenu) {
            subMenu.style.display = 'block';
        }
    }
});

function close() {
    let s = document.getElementsByClassName('submenu');
    for (let i = 0; i < s.length; i++) {
        s[i].style.display = 'none';
    }
}