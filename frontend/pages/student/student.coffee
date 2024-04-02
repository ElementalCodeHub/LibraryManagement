_id = localStorage.getItem("_id")
fetch(process.env.USERAPI+_id)
    .then((response) ->
      response.json()
    )
    .then((data) ->
    #   console.log("Data:", data)
        document.getElementById("name").innerText=data.name
        document.title="Student: "+data.name+" || Dashboard"
        document.getElementById("username").innerText="username: "+data.username
)