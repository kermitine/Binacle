(function () {
  const params = new URLSearchParams(window.location.search);
  if (params.get("embed") !== "1" || window.parent === window) return;

  const messageType = "binacle:resize";
  let pending = false;

  function getDocumentHeight() {
    const body = document.body;
    const html = document.documentElement;

    return Math.ceil(Math.max(
      body ? body.scrollHeight : 0,
      body ? body.offsetHeight : 0,
      html ? html.clientHeight : 0,
      html ? html.scrollHeight : 0,
      html ? html.offsetHeight : 0
    ));
  }

  function postSize() {
    pending = false;
    window.parent.postMessage({
      type: messageType,
      height: getDocumentHeight()
    }, "*");
  }

  function queuePostSize() {
    if (pending) return;
    pending = true;
    window.requestAnimationFrame(postSize);
  }

  window.addEventListener("load", queuePostSize);
  window.addEventListener("resize", queuePostSize);
  document.addEventListener("DOMContentLoaded", queuePostSize);

  if ("ResizeObserver" in window) {
    const resizeObserver = new ResizeObserver(queuePostSize);
    resizeObserver.observe(document.documentElement);
    if (document.body) resizeObserver.observe(document.body);
  }

  if ("MutationObserver" in window) {
    new MutationObserver(queuePostSize).observe(document.documentElement, {
      attributes: true,
      childList: true,
      subtree: true
    });
  }

  queuePostSize();
  window.setTimeout(queuePostSize, 250);
  window.setTimeout(queuePostSize, 1000);
  window.setTimeout(queuePostSize, 2500);
}());
