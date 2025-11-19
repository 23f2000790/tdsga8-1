---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  /* Custom Theme Specification via CSS */
  section {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 28px;
    color: #333;
  }
  h1 {
    color: #2B547E;
    border-bottom: 3px solid #2B547E;
    padding-bottom: 10px;
  }
  code {
    background-color: #f4f4f4;
    color: #d63384;
    padding: 2px 5px;
    border-radius: 4px;
  }
---

<!-- _class: lead -->
<!-- _backgroundColor: #2B547E -->
<!-- _color: white -->

# API v2.0 Documentation
## Technical Reference Guide

**Created by:** Technical Writing Team
**Contact:** [23f2000790@ds.study.iitm.ac.in](mailto:23f2000790@ds.study.iitm.ac.in)

---

<!-- header: 'System Architecture' -->
# Overview

This documentation covers the transition to the new RESTful architecture.

- **Scalability:** Horizontal scaling via load balancers.
- **Security:** OAuth 2.0 implementation.
- **Versioning:** Semantic versioning applied to all endpoints.

---

<!-- header: 'Performance Metrics' -->
# Algorithmic Complexity

We have optimized the search query engine. Below is the breakdown of the time complexity improvement for the database lookup algorithm.

The previous linear search was inefficient for large datasets:
$$ T(n) = O(n) $$

The new binary search implementation reduces latency significantly:
$$ T(n) = O(\log n) $$

*Where $n$ represents the number of records in the database.*

---

<!-- 
_class: lead 
_color: white
_text-shadow: 2px 2px 4px black
-->

![bg brightness:0.6](https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1920&auto=format&fit=crop)

# Infrastructure
## Hosted on Kubernetes Clusters

---

<!-- header: 'Configuration' -->
# Custom Directives Example

We use Marp directives to control the layout of specific slides.

1. **Maintainability:** This file is standard Markdown.
2. **Version Control:** Git tracks changes line-by-line.
3. **Export:** PDF, PPTX, and HTML are auto-generated via CI/CD.

> "Good documentation is like a tour guide; it should know where you are going before you do."

---

<!-- header: '' -->
<!-- _class: lead -->

# Q&A

Thank you for reviewing the documentation plan.

**Email:** 23f2000790@ds.study.iitm.ac.in
