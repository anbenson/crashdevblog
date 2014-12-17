$(document).ready(function() {
  $(".entry-toggle").click(function() {     
    $(this).siblings(".entry-content").slideToggle();
  });
});

var blogEntryHTML = '<div class="entry-header">\
                    <div class="entry-title">\
                      <h2>__TITLE__</h2>\
                    </div>\
                    <div class="entry-metadata">\
                      <div class="entry-author">\
                        <p class="entry-author">__AUTHOR__</p>\
                      </div>\
                      <div class="entry-date">\
                        <p class="entry-date">__DATETIME__</p>\
                      </div>\
                    </div>\
                  </div>\
                  <div class="entry-content">\
                    <p class="entry-description">__TEXT__</p>\
                  </div>\
                  <div class="entry-toggle">\
                    <p>\
                      click here to show/hide\
                    </p>\
                  </div>';
                  

var createBlogEntry = function(author, title, text, datetime) {
  var text =  blogEntryHTML.replace("__AUTHOR__",
                    author).replace("__TITLE__",
                     title).replace("__TEXT__",
                      text).replace("__DATETIME__", datetime);
  var node = document.createElement("div");
  node.setAttribute("class", "blog-entry");
  node.innerHTML = text;
  return node;
}

var addBlogEntry = function(entry) {
  var blogEntryContainer = document.getElementById("blog-entry-container");
  blogEntryContainer.appendChild(entry);
}

var emptyBlogEntries = function(entry) {
  var blogEntryContainer = document.getElementById("blog-entry-container");
  blogEntryContainer.innerHTML = "";
}