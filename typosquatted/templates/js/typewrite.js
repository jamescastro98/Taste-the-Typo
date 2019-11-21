const app = document.getElementById("app");
const typewriter = new Typewriter(app, {
  loop: false,
  delay: 75
});

typewriter
  .pauseFor(2500)
  .typeString("Taste the Typo: A TpyoSquatting Detector.")
  .pauseFor(300)
  .deleteChars(22)
  .typeString("ypoSquatting Detector.")
  .pauseFor(1000)
  .start();