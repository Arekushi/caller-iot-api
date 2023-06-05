/*
  Warnings:

  - Changed the type of `start_hour` on the `subject` table. No cast exists, the column would be dropped and recreated, which cannot be done if there is data, since the column is required.
  - Changed the type of `end_hour` on the `subject` table. No cast exists, the column would be dropped and recreated, which cannot be done if there is data, since the column is required.

*/
-- AlterTable
ALTER TABLE "attendance" ALTER COLUMN "created_at" SET DATA TYPE TIMESTAMP(3);

-- AlterTable
ALTER TABLE "student" ALTER COLUMN "updated_at" SET DATA TYPE TIMESTAMP(3),
ALTER COLUMN "created_at" SET DATA TYPE TIMESTAMP(3);

-- AlterTable
ALTER TABLE "subject" DROP COLUMN "start_hour",
ADD COLUMN     "start_hour" TIME NOT NULL,
DROP COLUMN "end_hour",
ADD COLUMN     "end_hour" TIME NOT NULL,
ALTER COLUMN "created_at" SET DATA TYPE TIMESTAMP(3),
ALTER COLUMN "updated_at" SET DATA TYPE TIMESTAMP(3);
