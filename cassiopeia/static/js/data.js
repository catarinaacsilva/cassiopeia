function handleDeletion(id, anon) {
    console.log(id+' '+anon);
    const base = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port
    console.log(base);
    const target = new URL('/confirmDeletion/', base);
    const params = new URLSearchParams();
    params.set('stayid', id);
    params.set('anonymize', anon)
    target.search = params.toString();
    console.log(target);

    const xhr = new XMLHttpRequest();
    xhr.open("DELETE", target, true);

    xhr.onload = function () {
        if (xhr.readyState == 4) {
            if (parseInt(xhr.status / 100) == 2) {
                console.log('OK:' + xhr.status);
                console.log(xhr.response);
                window.location.reload();
            } else {
                console.error(xhr.statusText);
            }
        }
    };

    xhr.send(null);
}