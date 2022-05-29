[WEB DESIGN CERTIFICATION](https://www.freecodecamp.org/learn/2022/responsive-web-design/)
## Learn HTML by building a Cat photo App
 
#### Step 1 
HTML elements have opening tags like ```<h1>``` and closing tags like ```</h1>```.
Find the h1 element and change the text between its opening and closing tags to say ***CatPhotoApp***.
 ```<h1>Hello World</h1>``` --> ```<h1>CatPhotoApp</h1>```

#### Step 2
The h1 to h6 heading elements are used to signify the importance of content below them. The lower the number, 
the higher the importance, so h2 elements have less importance than h1 elements. 
Only use one h1 element per page and place lower importance headings below higher importance headings.

Add an h2 element below the h1 element that says Cat Photos.
 
 ```<h1>CatPhotoApp</h1>```
 
 ```<h2>Cat Photos</h2>```
 
 Step 3

Paragraph (p) elements are used to create paragraph text on websites.

Create a paragraph (p) element below your h2 element, and give it the text Click here to view more cat photos.

<h2>Cat Photos</h2>

<p>Click here to view more cat photos.</p>

Step 4

Commenting allows you to leave messages without affecting the browser display. It also allows you to make code inactive. A comment in HTML starts with <!--, contains any number of lines of text, and ends with -->. For example, the comment <!-- TODO: Remove h1 --> contains the text TODO: Remove h1.

Add a comment above the p element with the text TODO: Add link to cat photos.

<!--TODO: Add link to cat photos-->

<p>Click here to view more cat photos.</p>

Step 5

HTML5 has some elements that identify different content areas. These elements make your HTML easier to read and help with Search Engine Optimization (SEO) and accessibility.

Identify the main section of this page by adding a <main> opening tag after the h1 element, and a </main> closing tag after the p element.

<h1>CatPhotoApp</h1>
<main>
<h2>Cat Photos</h2>
<!-- TODO: Add link to cat photos -->
<p>Click here to view more cat photos.</p>
</main>

Step 6

HTML elements are often nested within other HTML elements. In the previous step you nested the h2 element, comment and p element within the main element. A nested element is a child of its parent element.

To make HTML easier to read, indent the h2 element, the comment, and p element exactly two spaces to indicate they are children of the main element.

      <h2>Cat Photos</h2>
      <!-- TODO: Add link to cat photos -->
      <p>Click here to view more cat photos.</p>

Step 7

You can add images to your website by using the img element. img elements have an opening tag without a closing tag. A tag for an element without a closing tag is known as a self-closing tag.

Add an img element below the p element. At this point, no image will show up in the browser.

      <p>Click here to view more cat photos.</p>
      <img>
      
Step 8

HTML attributes are special words used inside the opening tag of an element to control the element's behavior. The src attribute in an img element specifies the image's URL (where the image is located). An example of an img element using an src attribute: <img src="https://www.your-image-source.com/your-image.jpg">.

Add an src attribute to the existing img element that is set to the following URL: https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg.

     <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg">
     
Step 9

All img elements should have an alt attribute. The alt attribute's text is used for screen readers to improve accessibility and is displayed if the image fails to load. For example, <img src="cat.jpg" alt="A cat"> has an alt attribute with the text A cat.

Add an alt attribute to the img element with the text A cute orange cat lying on its back.
      <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="A cute orange cat lying on its back">
      
Step 10

You can link to another page with the anchor (a) element. For example, <a href='https://freecodecamp.org'></a> would link to freecodecamp.org.

Add an anchor element after the paragraph that links to https://freecatphotoapp.com. At this point, the link won’t show up in the preview.

      <p>Click here to view more cat photos.</p>
      <a href='https://freecatphotoapp.com'></a>
      
Step 11

A link's text must be placed between the opening and closing tags of an anchor (a) element. For example, <a href="https://www.freecodecamp.org">click here to go to freeCodeCamp.org</a> is a link with the text click here to go to freeCodeCamp.org.

Add the anchor text cat photos to the anchor element. This will become the link's text.

      <a href="https://freecatphotoapp.com">cat photos</a>
      
Step 12

Turn the words cat photos located inside p element into a link by replacing the words with the anchor element added previously. The p element should show the same text in the browser, but the words cat photos should now be a link. There should only be one link showing in the app.




      






