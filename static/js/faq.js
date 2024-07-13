let faqs=document.getElementsByClassName('faq');
console.log(faqs.length);
for(let i=1;i<faqs.length + 1;i++){
    console.log(`faq-plus-${i}`);
    
    let plus=document.getElementById(`faq-plus-${i}`)

    plus.addEventListener('click',function(){

        document.getElementById(`faq-detail-${i}`).classList.toggle('hidden');
        console.log(plus.src);
        "/static/images/icons/"
        if(plus.src.includes('material-symbols-light_add.svg')){
            plus.src=plus.src.replace('material-symbols-light_add.svg','ic_outline-minus.svg');
        }else{
            plus.src=plus.src.replace('ic_outline-minus.svg','material-symbols-light_add.svg');
        }

        
    })
    
}