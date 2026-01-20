setInterval(() => {
    fetch("/logs-data")
    .then(res => res.text())
    .then(data => {
        document.getElementById("logBox").innerHTML = data;
    });
}, 2000);
