<h1> Sidewalk Obstruction Detection using Pre-Trained ResNet-50 Model </h1>
<h3> This repo contains all the files used for our DIP research project during our midyear term at Pamantasan ng Lungsod ng Maynila. By using images of streets in Intramuros, Manila, we were able to create a model that is capable of detecting sidewalk obstructions commonly found in the Philippines, specifically Metro Manila. </h3>
<hr>
<p> This project relies heavily on <a href="https://github.com/facebookresearch/detectron2"> Detectron2 </a> for model training and
  testing, as well as its possible future deployment. </p>
<p> Dataset images were acquired using Google Street View of some of the streets of intramuros. To maximize the sidewalk capture, the view was configured to show a 1-point perspective of the street, and then manually saved by printing the page or by using Windows' snipping tool. These images were then batch processed and downscaled to a standard resolution of 480p wide. </p>
<p> Dataset annotation was done using <a href="https://cvat.org/">CVAT</a>. </p>
<p> During the manual evaluation of street images, we identified 14 classes of obstructions:</p>
<ol>
  <li>Sidewalk</li>
  <li>Person</li>
  <li>Tree</li>
  <li>Post</li>
  <li>Sign</li>
  <li>Vehicle</li>
  <li>Pedicab</li>
  <li>Tricycle</li>
  <li>Bicycle</li>
  <li>Motorcycle</li>
  <li>Pothole</li>
  <li>Vendor Stall</li>
  <li>Plant Pot</li>
  <li>Debris</li>
</ol>
<p> After annotating these classes, the dataset was converted into COCO format using <a href="https://roboflow.com/">RoboFlow</a>. We also used RoboFlow to generate augmentations and further resized the images to create another dataset with the images resized to a square resolution of 416x416.</p>
