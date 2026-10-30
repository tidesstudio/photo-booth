# Postcard Photo Booth

A free Squarespace 7.1 plugin by [Tides Studio](https://tidesstudio.com). Visitors take a selfie and keep it as a postcard in your colour look. Photos are processed in the visitor's browser only. Nothing is uploaded or stored.

Get your booth code from the setup page: https://tidesstudio.com/postcard-photobooth

## Install

1. **Booth code.** Add a Code block where you want the booth, set it to HTML, turn off "Display Source", and paste in the booth code from the setup page.
2. **Styles.** Go to Website → Website Tools → Custom CSS, paste the styles from the setup page at the bottom and save.
3. **Script.** Go to Website → Website Tools → Code Injection → Footer, paste this line and save:

```html
<script src="https://cdn.jsdelivr.net/gh/tidesstudio/photo-booth@2.2.0/photo-booth.min.js"></script>
```

Requires a Squarespace plan with Code Injection (Core, Plus or Advanced).

## Updates

Each version has its own address, so your site only changes when you choose. To update, change the version number in the line above to the latest release.

## Files

- `photo-booth.js`: the readable source
- `photo-booth.min.js`: the file sites load

© Tides Studio. All rights reserved.
