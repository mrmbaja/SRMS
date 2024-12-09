function addCourseMark() {
    var container = document.getElementById('courseMarksContainer');
    var div = document.createElement('div');
    div.classList.add('course-mark');

    var courseInput = document.createElement('input');
    courseInput.setAttribute('type', 'text');
    courseInput.setAttribute('name', 'course[]');
    courseInput.setAttribute('placeholder', 'Course');

    var marksInput = document.createElement('input');
    marksInput.setAttribute('type', 'text');
    marksInput.setAttribute('name', 'marks[]');
    marksInput.setAttribute('placeholder', 'Marks');

    var removeButton = document.createElement('button');
    removeButton.setAttribute('type', 'button');
    removeButton.textContent = 'Remove';
    removeButton.setAttribute('onclick', 'removeCourseMark(this)');

    div.appendChild(courseInput);
    div.appendChild(marksInput);
    div.appendChild(removeButton);

    container.appendChild(div);
}

function removeCourseMark(button) {
    var div = button.parentElement;
    div.remove();
}
