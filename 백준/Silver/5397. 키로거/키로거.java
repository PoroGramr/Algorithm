import java.io.*;

public class Main {

    static class Node {
        char data;
        Node prev, next;

        Node(char data) {
            this.data = data;
        }
    }

    // cursor 뒤에 node 삽입
    static void insert(Node cursor, Node node) {
        node.prev = cursor;
        node.next = cursor.next;
        cursor.next.prev = node;
        cursor.next = node;
    }

    // node 삭제
    static void delete(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();

        
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            String input = br.readLine();

            // 더미 노드
            Node head = new Node('\0');
            Node tail = new Node('\0');
            head.next = tail;
            tail.prev = head;

            Node cursor = head;

            for (char c : input.toCharArray()) {
                if (c == '<') {
                    if (cursor != head) {
                        cursor = cursor.prev;
                    }
                } else if (c == '>') {
                    if (cursor.next != tail) {
                        cursor = cursor.next;
                    }
                } else if (c == '-') {
                    if (cursor != head) {
                        Node toDelete = cursor;
                        cursor = cursor.prev;
                        delete(toDelete);
                    }
                } else {
                    Node newNode = new Node(c);
                    insert(cursor, newNode);
                    cursor = newNode;
                }
            }

            // 결과 출력
            Node cur = head.next;
            while (cur != tail) {
                out.append(cur.data);
                cur = cur.next;
            }
            out.append('\n');
        }

        System.out.print(out);
    }
    

    
}
