console.log("fuck this mein, this is so weird")

var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var fileContent = xhr.responseText;
        document.getElementById('output').textContent = fileContent;
    }
};

xhr.open('GET', "sleep_on_the_floor.SRT", true);
xhr.send();

console.log(xhr);