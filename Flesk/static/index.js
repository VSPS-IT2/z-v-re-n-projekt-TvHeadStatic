array_of_posts = array_of_posts.replaceAll("&#39;", '"')

console.log(array_of_posts)

const obj = JSON.parse(array_of_posts);
   obj.forEach((element) => {
      document.getElementById('theseposts').innerHTML += `
      <article> 
            <h2>${element[0]}</h2> 
            <p> 
               ${element[1]} 
            </p> 
            <p> 
               ${element[2]}
            </p> 
      </article> 
      `
})