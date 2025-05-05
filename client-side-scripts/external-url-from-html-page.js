// biome-ignore lint/complexity/useArrowFunction: Use function keyword for legacy support.
(function () {
    const currentHost = window.location.host;
    const html = document.documentElement.innerHTML;

    // Regex to find all http(s) URLs
    const urlRegex = /https?:\/\/[^\s"'<>]+/g;
    const allMatches = Array.from(html.matchAll(urlRegex), m => m[0]);

    // Filter external URLs and dedupe
    const externalUrls = [...new Set(
        allMatches.filter(href => {
            try {
                const url = new URL(href);
                return (url.protocol === 'http:' || url.protocol === 'https:')
                    && url.host !== currentHost;
            } catch (e) {
                return false;
            }
        })
    )];

    // Prepare JSON blob
    const dataStr = JSON.stringify({ externalUrls }, null, 2);
    const blob = new Blob([dataStr], { type: 'application/json' });
    const blobUrl = URL.createObjectURL(blob);

    // Trigger download
    const dl = document.createElement('a');
    dl.href = blobUrl;
    dl.download = 'external-urls.json';
    document.body.appendChild(dl);
    dl.click();
    document.body.removeChild(dl);
    URL.revokeObjectURL(blobUrl);

    console.log(`Found ${externalUrls.length} external URLs.`);
})();
