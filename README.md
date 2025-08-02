# 🛒 Conscious Cart – AI-Powered Eco Product Analyzer

Conscious Cart helps consumers make **environmentally conscious** shopping decisions. Given a **product URL or name**, it analyzes the product’s sustainability profile using **Google’s Gemini LLM** and provides **eco-friendly alternatives** if needed.

> ♻️ "Buy smarter, live greener."

---

## 🌟 Features

- 🔗 Accepts product **URLs** (e.g. from Amazon) or **text names**
- 🌐 **Scrapes product pages** for title & feature list
- 🧠 Uses **Google Gemini (1.5 Flash)** to:
  - Generate plausible product info (if no URL provided)
  - Perform **environmental impact analysis**
  - Recommend **sustainable alternatives**
- ⚙️ **LangGraph & LangChain** powered workflow
- ✅ Command-line interface

---

## 🧠 Example Output

```text
## Product Analysis 📉

The GHAR SOAPS Magic Soap presents a mixed environmental profile...

NOT RECOMMENDED

## Better, Eco-Friendly Alternatives 🌱

1. **Dr. Bronner's Castile Soap** – Organic, Fair Trade ingredients...
2. **Ethique Solid Bars** – Plastic-free, sustainable supply chain...
3. **Homemade Soap** – Fully DIY, packaging-free, zero-waste...
