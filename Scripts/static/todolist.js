function Calendar(){
    var yes = confirm('Are you sure you want to go back? Whatever unsaved inputs will be erased!')
    if (yes == true){
        window.location.replace('../schedule');
    }
}
