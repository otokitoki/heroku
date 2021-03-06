  var resultList = document.getElementById("result");
  var dataList = localStorage.getItem("goku");  
  
  if(dataList){
    dataList = JSON.parse(dataList);
    dataList.forEach(appendNewData);
  }else{
    dataList = [];
  }

  function appendNewData(data) {
    const newListItem = document.createElement("li");
    newListItem.innerText = data.name + " " + data.category + " " + data.strength;
    resultList.appendChild(newListItem);
  }
  
  function appendbtn_click(){
    var data = {
        name:document.querySelector("#name").value,
        category:document.querySelector("#category").value,
        strength:document.querySelector("#strength").value
    };
    dataList.push(data);
    localStorage.setItem("goku", JSON.stringify(dataList));
    appendNewData(data)
    document.form1.reset();
  }


  document.querySelector("#appendbtn").addEventListener("click",
    appendbtn_click, false
  );

  document.querySelector("#form1").addEventListener("keypress",
    function(e) {
      if (e.keyCode === 13) {
        appendbtn_click();
      }
    }, false
  );


  document.querySelector("#deletebtn").addEventListener("click",
    function() {
      localStorage.clear();
      var element = document.getElementById("result");
      while (element.firstChild) {
        element.removeChild(element.firstChild);
      }
    }, false
  );
