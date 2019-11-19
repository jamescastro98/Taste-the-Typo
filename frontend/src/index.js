import Typewriter from "typewriter-effect/dist/core";
import GraphemeSplitter from "grapheme-splitter";

const app = document.getElementById("app");

const stringSplitter = string => {
  const splitter = new GraphemeSplitter();
  return splitter.splitGraphemes(string);
};

const typewriter = new Typewriter(app, {
  loop: false,
  delay: 75,
  stringSplitter
});

typewriter
  .pauseFor(2500)
  .typeString("Taste the Typo: A TpyoSquatting Detector.")
  .pauseFor(300)
  .deleteChars(22)
  .typeString("ypoSquatting Detector.")
  .pauseFor(1000)
  .start();
