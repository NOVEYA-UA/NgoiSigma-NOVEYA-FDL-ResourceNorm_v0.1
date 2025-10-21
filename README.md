# NOVEYA · Σ‑FDL::Δ‑Resource‑Normativity — MVP Pack (v2.1 Harmonized)

**Purpose:** пилотный модуль для AIB и других GVC‑структур, интегрирующий FDL‑нормирование ресурсов, мультиагентное поведение и параметры участия.

## Кратко
FDL‑модуль, который внедряет **осмысленное нормирование** расхода ресурсов в глобальные цепочки добавленной стоимости (GVC).
Поверх классических стратегий (scanning, supplier flexibility, redundancy) модуль добавляет **правила расхода**, **триггеры корректировок** и **аудит устойчивости**.

### Почему сейчас
- GVC перешла к «гибкости через избыточность», но игнорирует **устойчивую норму потребления**.
- AI ускоряет реакцию, но редко отвечает: **сколько потреблять разумно?**
- Σ‑FDL закрывает этот пробел: соединяет норму ↔ поток ↔ разум.

### Что даём
1. **Σ‑FDL‑токены** с нормами/правилами (машиночитаемо).
2. **Норм‑движок** (`norm_engine.py`) для расчётов и триггеров.
3. **API‑контракт** (мультиагентный обмен событиями/статусами).
4. **Аудит и отчётность** (периодический контроль и рекомендации).

---

## Архитектура
```
Data Sources (ERP/WMS/EMS) → Adapter → Norm Engine → Token Registry →
  → Event Hub (Actions) → Dash/API (agents)
```

- **Token Registry**: хранилище Σ‑FDL токенов с нормами, формулами, триггерами.
- **Norm Engine**: вычисляет нормативы, сравнивает с фактом, выдаёт события.
- **Adapters**: коннекторы к данным (логистика, склад, энергия, закупки).
- **Dash/API**: события/метрики наружу (в их AI/оркестратор).

---

## KPI пилота (пример)
- −8…12% переменных расходов (энергия/логистика) за 3 мес.
- −20…35% «мертвых» запасов без роста риска дефицита.
- −30% времени реакции на сбоевую ситуацию (lead‑time всплески).

---

## Σ‑FDL токены (машиночитаемые скелеты)
См. каталог [`tokens/`](tokens).

- `tokens/resource_normativity.yaml`
- `tokens/participation_boundary.yaml`

---

## API (контракт событий — упрощённо)
См. `openapi.yaml` и `api/server.py` (FastAPI).

```
POST /events/telemetry  { site_id, ts, metric, value, unit }
POST /events/order      { sku, qty, eta, supplier_id }
GET  /norms/{resource}/current → { formula_id, params, norm_value, time_window }
POST /actions/apply     { action_id, context }
```

---

## Условия пилота
- Доступ к агрегированным данным.
- Контракт: бюджет пилота / или rev‑share + право на публикацию кейса.
- Совместная команда: по 1 ответственному со стороны AIB и NOVEYA.

---

## Лицензии

## License & Ethics

This repository follows a dual-license scheme:

- **Code:** AGPL-3.0  
- **Content / Symbols / Media:** CC BY-NC-SA 4.0  
- **Ethical charter:** see [LICENSE-ETHICS.md](./LICENSE-ETHICS.md)

Use of FDL/NOVEYA symbols is allowed **only** in open, benevolent contexts; closed or exploitative usage is prohibited.

- **Методология**: права за NOVEYA (см. `METHODOLOGY_LICENSE.txt`).

---

## Содержание репозитория
- `README.md` — этот файл.
- `tokens/` — FDL‑токены норм и участия.
- `src/noveya_fdl/` — исходный код (ядро и модули).
- `api/server.py` — FastAPI сервер.
- `openapi.yaml` — спецификация API.
- `examples/` — примеры использования.
- `docs/` — архитектура, питч и 1‑пейджер.
- `unicode/glyphs.json` — заготовка глифов Unicode.
- `tests/` — базовые тесты.
- `pyproject.toml` — упаковка как Python‑пакет.

---

© 2025-09-25 NGOI‑SIGMA (AZ) / NOVEYA · Protonovea
