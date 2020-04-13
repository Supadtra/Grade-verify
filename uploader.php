
<html>
<title>Call API</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<style>
.imgcontainer {
  text-align: center;
  margin: 24px 0 200px 0;
  position: relative;
  padding: 200px;
}


</style>
<body>
    <div class="modal-content animate">
      <form action = "http://localhost:5000/uploader" method = "POST" 
         enctype = "multipart/form-data">
         <center><div class="imgcontainer">
                <input type="file" name="file" id="file" accept=".csv">
                <br><br>
                <button type="submit" id="submit" name="add" class="btn-submit" >ADD</button>
         </div></center>
         
      </form>   
   </body>
</html>
