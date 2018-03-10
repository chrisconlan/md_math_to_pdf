---
title: "Test PDF Rendered from Math Markdown"
subtitle: "A Subtitle"
author: "Chris Conlan"
date: "March 9, 2018"
output:
  pdf_document: default
geometry: margin=1in
graphics: yes
---


# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6

http://example.com/auto-linked-url

Some text...

**bold**

*slanty*

`monoscript`

**`bold monoscript`**

```python
# Python highlighted syntax
import numpy as np
print(np.arange(1,10))

"""
Some nice python docstrings
"""
```

A regression...

$$
\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_{i,1} + \hat{\beta}_2 x_{i,2} + ... + \hat{\beta}_n x_{i,n}
$$

Now some $\alpha$ inline $\beta$ math $\gamma$ with $\delta$ lot $\eta$ of $\zeta$ Greek.

![Jazz Dog](./jazz_dog.jpeg)




