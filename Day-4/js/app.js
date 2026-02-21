const btn = document.getElementById("themeToggle");

if(localStorage.getItem("theme") === "dark"){
    document.body.classList.add("dark");
    btn.textContent=" ";
}

btn.onclick = () =>{
    document.body.classList.toggle("dark");

    if(document.body.classList.contains("dark")){
        localStorage.setItem("theme","dark");
        btn.textContent=" ";
    }else{
        localStorage.setItem("theme","light");
        btn.textContent=" ";
    }
}
