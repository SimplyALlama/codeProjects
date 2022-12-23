var roomWidth = 0;
var roomLength = 0;

class furniture
{
	constructor(width, length, name, colour, locationX, locationY)
	{
		this.width = width;
		this.length = length;
		this.name = name;
		this.colour = colour;
		this.locationX = locationX;
		this.locationY = locationY;
	}

	get Width()
	{
		return this.width;
	}

	get Length()
	{
		return this.length;
	}

	get Name()
	{
		return this.name;
	}

	get Colour()
	{
		return this.colour;
	}

	get location()
	{
		return this.locationX, this.locationY;
	}
}

function drag()
{
	// The current position of mouse
	let x = 0;
	let y = 0;

	// Query the element
	const ele = document.getElementById('block');

	// Handle the mousedown event
	// that's triggered when user drags the element
	const mouseDownHandler = function (e) {
		// Get the current mouse position
		x = e.clientX;
		y = e.clientY;

		// Attach the listeners to `document`
		document.addEventListener('mousemove', mouseMoveHandler);
		document.addEventListener('mouseup', mouseUpHandler);
	};

	const mouseMoveHandler = function (e) {
		// How far the mouse has been moved
		const dx = e.clientX - x;
		const dy = e.clientY - y;

		// Set the position of element
		ele.style.top = `${ele.offsetTop + dy}px`;
		ele.style.left = `${ele.offsetLeft + dx}px`;

		// Reassign the position of mouse
		x = e.clientX;
		y = e.clientY;
	};

	const mouseUpHandler = function () {
		// Remove the handlers of `mousemove` and `mouseup`
		document.removeEventListener('mousemove', mouseMoveHandler);
		document.removeEventListener('mouseup', mouseUpHandler);
	};

	ele.addEventListener('mousedown', mouseDownHandler);
}