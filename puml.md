[https://github.com/GitbookIO/plugin-puml](https://github.com/GitbookIO/plugin-puml)



Then in your content:

```
This is a diagram:

{% plantuml %}
Bob-
>
Alice : hello
{% endplantuml %}
```

The plugin will replace the`{% plantuml %}`by SVG images \(and PNG images for ebook output\).

