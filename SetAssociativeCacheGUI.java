import javax.swing.*;
import javax.swing.border.TitledBorder;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.LinkedList;

public class SetAssociativeCacheGUI extends JFrame {

    // --- Configuration ---
    private static final int NUM_SETS = 4; // Number of Rows
    private static final int WAYS = 2;     // Number of Columns (2-way associative)

    // --- GUI Components ---
    private BlockPanel[][] cacheGrid;      // The 2D visual grid
    private JTextArea logArea;             // To show the math/logic steps
    private JTextField addressField;
    private JTextField dataField;
    
    // --- Cache Data Structures (Logic) ---
    // We use a simple counter for FIFO replacement for this demo
    private int[] replacementCounters; 

    public SetAssociativeCacheGUI() {
        setTitle("Set Associative Mapping Visualizer");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));

        replacementCounters = new int[NUM_SETS];

        // 1. TOP PANEL: Controls
        JPanel controlPanel = new JPanel(new FlowLayout());
        addressField = new JTextField(10);
        dataField = new JTextField(10);
        JButton writeBtn = new JButton("Write to Cache");
        
        controlPanel.add(new JLabel("Memory Address (Int):"));
        controlPanel.add(addressField);
        controlPanel.add(new JLabel("Data (String):"));
        controlPanel.add(dataField);
        controlPanel.add(writeBtn);

        add(controlPanel, BorderLayout.NORTH);

        // 2. CENTER PANEL: The 2D Cache Grid
        JPanel gridPanel = new JPanel(new GridLayout(NUM_SETS, 1, 10, 10)); // Rows of Sets
        gridPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        
        cacheGrid = new BlockPanel[NUM_SETS][WAYS];

        for (int i = 0; i < NUM_SETS; i++) {
            // Create a panel for the Set (Row)
            JPanel setPanel = new JPanel(new GridLayout(1, WAYS, 10, 0));
            setPanel.setBorder(BorderFactory.createTitledBorder(
                    BorderFactory.createLineBorder(Color.GRAY), "Set " + i));
            
            for (int j = 0; j < WAYS; j++) {
                BlockPanel block = new BlockPanel(j);
                cacheGrid[i][j] = block;
                setPanel.add(block);
            }
            gridPanel.add(setPanel);
        }
        
        // Wrap grid in scroll pane
        add(new JScrollPane(gridPanel), BorderLayout.CENTER);

        // 3. BOTTOM PANEL: Logs
        logArea = new JTextArea(8, 50);
        logArea.setEditable(false);
        logArea.setFont(new Font("Monospaced", Font.PLAIN, 12));
        add(new JScrollPane(logArea), BorderLayout.SOUTH);

        // 4. Action Listener Logic
        writeBtn.addActionListener(e -> processMemoryAccess());
        
        // Initialize with default values for quick testing
        addressField.setText("0");
        dataField.setText("A");
    }
