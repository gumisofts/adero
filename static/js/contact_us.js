document.getElementById("service-menu-button").addEventListener('click',function() {
    document.getElementById("service-dropdown").classList.toggle("hidden");
});

let services=document.getElementsByClassName("service-items");
for(let i=0;i<services.length;i++){
    services[i].addEventListener('click',function() {
        document.getElementById("service-dropdown").classList.toggle("hidden");
        let menubtn=document.getElementById("service-menu-button");
        let svg_icon=menubtn.children[0]
        menubtn.value=services[i].innerHTML;
        // menubtn.appendChild(svg_icon);
        // menubtn.value=services[i].value;
        console.log(menubtn)

    })
}