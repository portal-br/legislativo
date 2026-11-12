---
block: multiButtons
---

Shows a row of links as buttons, cards or images. Use it for shortcuts to important pages, such as the ombudsman, the agenda or the transparency portal. The block can also be placed inside the grid block.

The block stores its settings, and a list of buttons in its `buttons` field. Each button is an item of that list, and the fields an item uses depend on the block's `variant`. The fields that the variant does not use are ignored when the block is shown.

### Fields

- `variant`: how the buttons are shown. `default` shows buttons with an optional icon, `card` shows cards with a title and a description, and `image` shows buttons with an image. Defaults to `default` when omitted.
- `buttons`: the list of buttons. Each item is described below. The editor gives each item an `@id`.
- `maxColumns`: the maximum number of buttons per row, from 1 to 6. The editor starts with 3. When the field is omitted, all buttons are placed in one row. Small screens always show fewer buttons per row.
- `stretch`: `true` to make the buttons share the full width of the block. `false` or omitted to make every button as wide as the widest one.
- `theme`: the name of one of the site's block themes, which sets the background color of the block. When omitted, the block has no theme colors of its own.

### Fields of each button

- `title`: the text of the button, or the title of the card. In the `image` variant, it is the label read by screen readers.
- `description`: a text shown under the title of a card. Used by the `card` variant only.
- `href`: a list with one item, `[{ "@id": path or URL, "title": title }]`. Use a path for content from the site, or a full URL for an external link. A button without `href` is shown faded and cannot be clicked.
- `icon`: the name of the icon, one of `arrowRight`, `phone`, `user`, `summary`, `calendar`, `image`, `news`, `link`, `check` or `email`. Used by the `default` variant only. Leave it out for a button without an icon.
- `image`: a list with one item, in the same format as `href`, that points to the image of the button. Required by the `image` variant.
- `altText`: a text that describes what the button does, for example `Open the transparency portal`. Required by the `image` variant, where it is read by screen readers.
- `openInNewTab`: `true` to open the link in a new browser tab. `false` or omitted to open it in the same tab.

### Example

```json
{
  "@type": "multiButtons",
  "variant": "default",
  "buttons": [
    {
      "@id": "2f6c1c0e-3b8a-4c5e-9d1a-7e2b5a9f0c11",
      "title": "Ouvidoria",
      "icon": "phone",
      "href": [{ "@id": "/ouvidoria", "title": "Ouvidoria" }],
      "openInNewTab": false
    },
    {
      "@id": "8d4e9a7b-1f2c-4a3b-8e5d-6c9f0a1b2d34",
      "title": "Portal da transparência",
      "icon": "link",
      "href": [
        {
          "@id": "https://www.example.org/transparencia",
          "title": "Portal da transparência"
        }
      ],
      "openInNewTab": true
    }
  ],
  "maxColumns": 3,
  "stretch": false,
  "theme": "default"
}
```
