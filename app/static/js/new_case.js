"use strict";
//Disable Quaranteen Date input if test result is negativew
window.addEventListener("load", () => {
  const testResult = document.querySelector("#test-result");
  testResult.addEventListener("change", (event) => {
    const qStartDate = document.querySelector("#quaranteen-start-date");
    const qEndDate = document.querySelector("#quaranteen-end-date");
    if (testResult.value == "negativ") {
      qStartDate.disabled = true;
      qEndDate.disabled = true;
    } else {
      qStartDate.disabled = false;
      qEndDate.disabled = false;
    }
  });
});
