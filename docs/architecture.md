# Архитектура Σ‑FDL::Resource‑Norm

Data → Adapter → Norm Engine → Token Registry → Event Hub → Agents

- Adapter: извлечение и нормализация метрик.
- Norm Engine: вычисление норм, выявление отклонений.
- Token Registry: хранение токенов норм и правил.
- Event Hub: маршрутизация действий/сигналов.
- Agents: человек/ИИ/оркестраторы.
