"use strict";
//Disable Quaranteen Date input if test result is negativew
window.addEventListener("load", () => {
  const testResult = document.querySelector("#test-result");
  testResult.addEventListener("change", (event) => {
    const qStartDate = document.querySelector("#quarantine-start-date");
    const qEndDate = document.querySelector("#quarantine-end-date");
    if (testResult.value == "negativ") {
      qStartDate.disabled = true;
      qEndDate.disabled = true;
      qStartDate.value = null;
      qEndDate.value = null;
    } else {
      qStartDate.disabled = false;
      qEndDate.disabled = false;
    }
  });
});
