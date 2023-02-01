//Selecting the slider and putting it in a variable called slider
const slider = document.querySelector('.slider-container'), 
	//Selecting all as there is more than one slide and putting it into an array
	slides = Array.from(document.querySelectorAll('.slide')) 

//Setting global variables
let isDragging = false,
	StartPos = 0,
	//Starting position is wherever we click in th browser
	currentTranslate = 0,
	//Above refers to transform attribute in CSS within slider-container
	prevTranslate = 0,
	animationID = 0,
	currentIndex = 0
	//Index refers to the current slide

//Loop through the slides (images)
slides.forEach((slide, index) => 
{
	const slideImage = slide.querySelector('img')
	//Prevent default behaviour dragging image
	slideImage.addEventListener('dragstart', (e) => e.preventDefault())

	//Touch Events for mobile devices
	slide.addEventListener('touchstart', touchStart(index))
	//When you take your finger off the device
	slide.addEventListener('touchend', touchEnd)
	//When you have your finger on the device and are moving it around
	slide.addEventListener('touchmove', touchMove)



	//Mouse Events for browsers
	slide.addEventListener('mousedown', touchStart(index))
	//Letting go of the mouse
	slide.addEventListener('mouseup', touchEnd)
	//When mouse leaves the slide or the screen
	slide.addEventListener('mouseleave', touchEnd)
	//When your moving the image around
	slide.addEventListener('mousemove', touchMove)
})

//Make responsive to viewport changes
window.addEventListener('resize', setPositionByIndex)

//Disable context menu
window.oncontextmenu = function(event) 
{
	//Prevents default behaviour in menu popping up and when right clicking
	event.preventDefault()
	event.stopPropagation()
	return false
}

//Creating the functions for the event listeners above
function touchStart(index) 
{
	//Calling the function and returning it
	return function(event) 
	{
		//Setting index to the currentIndex
		currentIndex = index
		//Getting the starting position by mouse or touch
		startPos = getPositionX(event)
		isDragging = true

		//Animation the transition along the X axis using animationID
		animationID = requestAnimationFrame(animation)

		//To add grabbing
		slider.classList.add('grabbing')

	}
}

function touchEnd() 
{
	//Not required to return function here as there's nothing parsed here unlike index above
	isDragging = false
	//When image isn't being moved cancel the animation
	cancelAnimationFrame(animationID)

	//To snap onto the next image when user stops grabbing/touching
	const movedBy = currentTranslate - prevTranslate

	//If user has moved image 100px to the left and getting the total length of the array
	if(movedBy < -100 && currentIndex < slides.length - 1)
	currentIndex += 1

	//To move the slide to other side and making sure we're not on the first image to go the image on the left
	if(movedBy > 100 && currentIndex > 0)
	currentIndex -= 1

	setPositionByIndex()

	//To remove grabbing
	slider.classList.remove('grabbing')
}

function touchMove(event) 
{
	//Getting the current position taking event as an argument
	if(isDragging)
	{
		const currentPosition = getPositionX(event)
		//Vital for the function to animate in setSliderPosition() function
		currentTranslate = prevTranslate + currentPosition - startPos
	}
}

//Getting the starting position by mouse or touch
function getPositionX(event)
{
	return event.type.includes('mouse') ? event.pageX : event.touches[0].clientX
}

function animation()
{
	//Calling the animation function
	setSliderPosition()
	//If isDragging is true then request animation frame
	//Calling animation frame again is better for performance apparently
	if(isDragging) requestAnimationFrame(animation)
}

function setSliderPosition()
{
	//Current translate is 0 by default but will change dynamically as user moves image
	slider.style.transform = `translateX(${currentTranslate}px)`
}

function setPositionByIndex()
{
	//Inner width ensures it doesn't matter whether your window is stretched or not
	currentTranslate = currentIndex * -window.innerWidth
	prevTranslate = currentTranslate
	setSliderPosition()
}
