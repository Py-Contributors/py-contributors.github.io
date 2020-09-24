# py-contributors.github.io

<img style="height:200px; width:250px;" src="./assets/img/octojekyll.png" alt="Jekyll logo">

This website is created using jekyll.

Run website locally on your Pc.

```bash
gem install bundler jekyll
bundle exec jekyll serve
```

If you like to contribute to project and new to Jekyll Please go through the [Documentation](https://jekyllrb.com/).

Jekyll is a static site generator. It takes text written in your favorite markup language and uses layouts to create a static website. You can tweak the site's look and feel, URLs, the data displayed on the page, and more.



<div class="card mt-2 p-2">
  <h3 class="text-center"> <a href="{{ post.url }}">{{ post.title }}</a></h3>           
  <p class="text-dark text-center my-2">               
    <i class="fa fa-calendar"></i>{{post.date}}
    <i class="fa fa-user mx-1"></i> <a href="{{post.author_profile_link}}" target="_blank" >{{post.author}}</a>                     
  </p>
    <img class="img-fluid shadow" style="width: 800px;height: 300px;" src="{{post.image}}" alt="student_performance_prediction">
  <div class="container mt-1">              
    <p class="text-dark" style="font-size: 17px">{{post.subtitle}}</p>
    <a href="{{post.url}}" class="btn btn-primary">Read More...</a>				
</div>
</div>
<hr>