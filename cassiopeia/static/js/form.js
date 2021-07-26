function handleSubmit(event) {
  event.preventDefault();
  const path = event.target.action
  console.log(path);
  const data = new FormData(event.target);
  const values = Object.fromEntries(data.entries());
  console.log(values);
  const xhr = new XMLHttpRequest();
  xhr.open("POST", path, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  const body = JSON.stringify(values);
  xhr.send(body);
  
}

console.log('Register all forms....')
const forms = document.getElementsByTagName('form');
for (let i = 0; i < forms.length; i++) {
  forms[i].addEventListener('submit', handleSubmit);
}
