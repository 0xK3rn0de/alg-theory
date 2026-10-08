from package import Jacket, Trousers, ThreePieceSuit, save_report_to_docx

def main():
    print("=== Расчёт расхода ткани и стоимости пошива ===")
    print("Выберите изделие:")
    print("1 - Пиджак")
    print("2 - Брюки")
    print("3 - Костюм-тройка")

    choice = input("Ваш выбор (1/2/3): ").strip()
    if choice not in ('1', '2', '3'):
        print("Неверный выбор.")
        return

    size = int(input("Введите размер (например, 44, 46, 48...): "))
    fabric_price = float(input("Цена ткани за метр (руб.): "))
    accessories_cost = float(input("Стоимость фурнитуры (руб.): "))
    work_cost = float(input("Стоимость работы (руб.): "))

    if choice == '1':
        item = Jacket(size, fabric_price, accessories_cost, work_cost)
    elif choice == '2':
        item = Trousers(size, fabric_price, accessories_cost, work_cost)
    else:
        item = ThreePieceSuit(size, fabric_price, accessories_cost, work_cost)

    fabric = item.calculate_fabric()
    total_cost = item.calculate_total_cost()

    print("\n--- Результат ---")
    print(f"Изделие: {item.name}")
    print(f"Размер: {size}")
    print(f"Расход ткани: {fabric:.2f} м")
    print(f"Итоговая стоимость: {total_cost:.2f} руб.")

    # Сохранение отчёта
    save_choice = input("\nСохранить отчёт в .docx? (y/n): ").strip().lower()
    if save_choice == 'y':
        data = [{
            'name': item.name,
            'size': size,
            'fabric': fabric,
            'cost': total_cost
        }]
        save_report_to_docx(data, "clothing_report.docx")

if __name__ == "__main__":
    main()