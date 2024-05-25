function consult_user(){
    let id = document.getElementById("patnr").value
    let obj_id = {"patnr": id}
    fetch('/consult_user', {
        "method":"post",
        "headers":{"content-type":"application/json"},
        "body": JSON.stringify(obj_id)
    })
    .then(resp => resp.json())
    .then(data => {
        if (data.status == "ok") {
            obj_data = data.vname + " " + data.nname + " " + data.gbdat
            document.getElementById("txt_data").value = obj_data
        }
        else {
            alert("The user was not found")
        }
    })
    .catch(err => alert(err))
}    
    
    
//let id = document.getElementById("patnr").value
//let obj_id ={"patnr": id}

//function consult_user() {