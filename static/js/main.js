
function showServiceMenu(){
    document.getElementById('services-menu').classList.remove('hidden');

    document.getElementById('more-services-icon').classList.add('rotate-180');
}
function hideServiceMenu(){
    document.getElementById('services-menu').classList.add('hidden');
    document.getElementById('more-services-icon').classList.remove('rotate-180');

}
function toggleNavs(){
    document.getElementById('header').classList.toggle('h-max');
    document.getElementById('header-menu-more').classList.toggle('hidden');
    document.getElementById('header-menu-less').classList.toggle('hidden');
}