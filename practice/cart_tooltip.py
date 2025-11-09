import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.List;

public class CartApp extends JFrame {
    private JButton cartButton;
    private List<Item> cartItems;

    public CartApp() {
        super("Магазин");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setSize(400, 200);
        setLayout(new FlowLayout());

        // створюємо список товарів
        cartItems = new ArrayList<>();
        // приклад заповнення (можна закоментувати для тесту порожнього кошика)
        cartItems.add(new Item("Ноутбук", 3, 700));
        cartItems.add(new Item("Мишка", 2, 100));
        cartItems.add(new Item("Клавіатура", 2, 200));

        cartButton = new JButton("🛒 Кошик");
        add(cartButton);

        updateToolTip();

        // дія при натисканні
        cartButton.addActionListener(e -> showCartInfo());

        setVisible(true);
    }

    private void updateToolTip() {
        if (cartItems.isEmpty()) {
            cartButton.setToolTipText("У кошику немає товарів");
        } else {
            int positions = cartItems.size();
            int totalCount = cartItems.stream().mapToInt(Item::getQuantity).sum();
            double totalSum = cartItems.stream().mapToDouble(Item::getTotalPrice).sum();

            cartButton.setToolTipText(
                    String.format("<html>У вашому кошику позицій - %d<br>"
                            + "товарів - %d<br>"
                            + "на загальну суму %.2f грн<br>"
                            + "(натисніть для оформлення)</html>",
                            positions, totalCount, totalSum)
            );
        }
    }

    private void showCartInfo() {
        if (cartItems.isEmpty()) {
            JOptionPane.showMessageDialog(this, "У кошику немає товарів");
        } else {
            StringBuilder sb = new StringBuilder("Ваш кошик:\n");
            for (Item item : cartItems) {
                sb.append(String.format("%s — %d шт × %.2f грн = %.2f грн\n",
                        item.getName(), item.getQuantity(), item.getPrice(), item.getTotalPrice()));
            }
            sb.append("\nЗагальна сума: ")
              .append(cartItems.stream().mapToDouble(Item::getTotalPrice).sum())
              .append(" грн");
            JOptionPane.showMessageDialog(this, sb.toString());
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(CartApp::new);
    }
}

// Клас товару (ОOП)
class Item {
    private String name;
    private int quantity;
    private double price;

    public Item(String name, int quantity, double price) {
        this.name = name;
        this.quantity = quantity;
        this.price = price;
    }

    public String getName() { return name; }
    public int getQuantity() { return quantity; }
    public double getPrice() { return price; }

    public double getTotalPrice() {
        return quantity * price;
    }
}
