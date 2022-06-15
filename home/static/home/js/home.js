// if (document.location.pathname === '/') {
// 	let map = document.getElementById('osmap')
// 	map.addEventListener('', (event) =>{
// 		event.preventDefault()
// 		map.classList.toggle('enable')
// 	console.log(document.location.pathname === '/')
// 	})
// }

function postFormData(url, data, csrftoken) {
	return fetch(url, {
		method: "POST",
		body: data,
		headers: {"X-CSRFToken": csrftoken}
	})
}

const formEL = document.getElementById('main-search')
	// const searchInput = document.getElementById('search-input')
const map = document.getElementById("osmap-scroll")

formEL.addEventListener('submit', (event) => {
	const userInput = new FormData(event.target)
	const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
	event.preventDefault()
	postFormData("/", userInput ,csrftoken)
		.then(response => {
			console.log(response)
		})
})
if (map) {
	map.scrollIntoView({behavior: "smooth", block: "center"})
}



