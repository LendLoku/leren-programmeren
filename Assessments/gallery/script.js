const imageData = [ 
    "6.jpg", 
    "2023-lamborghini-urus_s-1.jpg", 
    "2024-mercedes-amg-c63-s-e-performance-exterior.jpg", 
    "aczy57nb19in_800.jpg", 
];

let count = 0;
let previous = document.getElementById("previous");
let next = document.getElementById("next");

let image = document.getElementById("image");

next.addEventListener("click", function click(){
    if (count == 3`9`){
        count = 0
    } else {
        count += 1;
    }
    image.src = imageData[count];
})

previous.addEventListener("click", function click(){
    if (count == 0){
        count = 3
    } else{
        count -= 1;
    }
    image.src = imageData[count];

})