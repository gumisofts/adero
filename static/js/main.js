
function showServiceMenu(){
    document.getElementById('services-menu').classList.remove('hidden');

    document.getElementById('more-services-icon').classList.add('rotate-180');
}
function hideServiceMenu(){
    document.getElementById('services-menu').classList.add('hidden');
    document.getElementById('more-services-icon').classList.remove('rotate-180');

}